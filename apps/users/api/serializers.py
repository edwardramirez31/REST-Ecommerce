from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        """
        This method is used to create a new user instance. In this case, is 
        overwritten in order to edit a field. 
        
        Default: Model.objects.create(**validated_data).
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Method used to update a user instance. This also adds functionality so
        that the password can be encrypted.

        Defaut: It uses a for loop and updates the fields passed in validated_data
        instance.field = validated_data.get('field', instance.field)
        """
        # updates all the fields with the super method
        user = super().update(instance, validated_data)
        # Adding the password functionality to a user updated
        user.set_password(validated_data['password'])
        user.save()
        return user

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        """
        This method receives each instance passed as data to the serializer.
        It's used to give another way to show the database information
        """
        # Each instance is a dictionary from the values method
        return {
            "id": instance["id"],
            "username": instance["username"],
            "password": instance["password"],
            "email": instance["email"],
        }

    

class TestSerializer(serializers.Serializer):
    # primero realiza las validaciones del campo como tal
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()

    # despues procede a las validaciones extras de cada campo
    def validate_name(self, value):
        return value

    def validate_email(self, value):
        email = value.split('@')[1].split('.')[0].lower()
        if email != 'gmail':
            raise serializers.ValidationError('Please enter a email from Google.')
        return value

    # finalmente, va a validacion extra general
    def validate(self, data):
        # it cannot have the dollar sign
        # si hubo un error con alguno de las anteriores validaciones, este metodo no se va a ejecutar (email o name)
        if '$' in data['name']:
            raise serializers.ValidationError({'name': "The name cannot contain a dollar sign"})
        return data
