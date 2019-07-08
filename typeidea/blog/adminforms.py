# -*- coding: utf-8 -*-


from django import  forms

class PostAdminForm(forms.ModelForm):
    # status= forms.BooleanField(label='是否删除',required=True) #TODO:处理布尔类型为我们需要的字段

    desc= forms.CharField(widget=forms.Textarea,label='摘要',required=False)

    # def clean_status(self):
    #     print(self.cleaned_data)
    #     if self.cleaned_data['status']:
    #         return 1
    #     else:
    #         return 3