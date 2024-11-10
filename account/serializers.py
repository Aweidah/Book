from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add this to handle password input securely

    class Meta:
        model = User
        fields = ['email','password']
        # fields = '__all__'  # or specify fields as a list like ['username', 'email']

    # Ensure the create method is correctly indented outside of the 'Meta' class
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            # username=validated_data['username'],
            # first_name=validated_data.get('first_name', ''),
            # last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
