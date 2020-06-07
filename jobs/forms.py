from cloudinary.forms import CloudinaryFileField
class AvatarUploadForm(forms.ModelForm):
    avatar = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'avatars'
       }
    )
    class Meta:
        model = Author
        fields = ('avatar',)
