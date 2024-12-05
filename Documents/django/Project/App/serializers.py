#checks for the data type
#convert data to python data
#serialize the data

# from rest_framework import serializers
# from .models import Student
# from django.core.validators import MaxValueValidator, MinValueValidator


# class StudentSerializers(serializers.ModelSerializer):
#     #table
#     first_name=serializers.CharField(max_length=100)
#     last_name=serializers.CharField(max_length=100)
#     section=serializers.IntegerField(
#         validators=[MinValueValidator(1),MaxValueValidator(12)]
#     )
#     roll_no=serializers.IntegerField()
    
#     class Meta:
#         model=Student
#         fields='__all__'
    
#     def validate_roll_no(self, value):
#         if Student.objects.filter(section=self.initial_data.get('section'), roll_no=value).exists():
#             raise serializers.ValidationError("This roll number is already assigned in this section.")
#         return value

#     # Object-level validation for additional cross-field logic
#     def validate(self, data):
#         section = data.get('section')
#         roll_no = data.get('roll_no')
        
#         if section > 10 and roll_no % 2 != 0:
#             raise serializers.ValidationError("For sections greater than 10, roll number must be even.")
        
#         return data
    
from rest_framework import serializers
from .models import Student,StudentContactInfo
 #table          serializers to validate and convert data between JSON and Python objects.
    
class StudentContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentContactInfo
        fields = [ 'email', 'phone_number']
    
    def validate_email(self, value):
        if StudentContactInfo.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already associated with another student.")
        return value

    def validate_phone_number(self, value):
        if StudentContactInfo.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("This phone number is already associated with another student.")
        return value
class StudentSerializers(serializers.ModelSerializer):
    contact_info=StudentContactInfoSerializer(many=True)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'section', 'roll_no','contact_info']
    def create(self, validated_data):
        contact_info_data = validated_data.pop('contact_info',[])
        student = Student.objects.create(**validated_data)
        for contact_data in contact_info_data:
            StudentContactInfo.objects.create(student=student, **contact_data)
        return student
    
    def validate_roll_no(self, value):
        # Example validation for unique roll_no in a section
        section = self.initial_data.get('section')
        if Student.objects.filter(roll_no=value, section=section).exists():
            raise serializers.ValidationError("Roll number already exists in this section.")
        return value

    def validate_section(self, value):
        # Example validation for section range
        if not (1 <= value <= 12):
            raise serializers.ValidationError("Section must be between 1 and 12.")
        return value
    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact_info', [])
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.section = validated_data.get('section', instance.section)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.save()
        for contact in contact_data:
            StudentContactInfo.objects.update_or_create(
                student=instance,
                email=contact.get('email'),
                defaults={'phone_number': contact.get('phone_number')}
            )
        return instance