from django.core.validators import RegexValidator

validate_only_letter_value = RegexValidator(r'^[a-zA-Z]*$', 'The value should contain only letters.')