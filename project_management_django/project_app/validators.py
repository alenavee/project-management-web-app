from django.core.exceptions import ValidationError
import magic


def validate_file_size(file):
    MAX_MB = 5
    limit = MAX_MB * 1024 * 1024

    if file.size > limit:
        raise ValidationError(f'The file size is more than {MAX_MB} MB.')


def validate_file_type(file):
    photo_extensions = ['image/png', 'image/jpeg', 'image/jpg']

    content_type = magic.from_buffer(file.read(), mime=True)
    if content_type not in photo_extensions:
        raise ValidationError(f'Files of type {content_type} are not supported.')