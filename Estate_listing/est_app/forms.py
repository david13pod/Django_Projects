from est_app.models import Property, Agent,Leads
from django import forms

class PropertyForm(forms.ModelForm):
    
    class Meta:
        model=Property
        fields=('title','picture','location','zipcode','price' ,'rooms', 'agent','description')
        widgets={ #set up classes to edit widget css
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'description':forms.Textarea(attrs={ 'class':'editable medium-editor-textarea pptcontent',}) 
        }

class AgentForm(forms.ModelForm):
    
    class Meta:
        model=Agent
        fields=('firstname','lastname','contact','email','pix')
        


class LeadsForm(forms.ModelForm):
    
    class Meta:
        model=Leads
        fields=('firstname','lastname','email','message')
        widgets={ #set up classes to edit widget css
            'message':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent leadcontent'}) 
        }