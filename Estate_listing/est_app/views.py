from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,DeleteView, CreateView,UpdateView
from est_app.models import Property, Agent,Leads
from est_app.forms import PropertyForm, AgentForm,LeadsForm
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q
# import re
# from django.utils.html import strip_tags
# Create your views here.

#main property views
# class HomeView(ListView):
#     model=Property

#     def get_queryset(self): #show 2 expensive listings
#         return Property.objects.filter(published_date__lte=timezone.now()).order_by('price')[:2]

class HomeView(TemplateView):
    model=Property

    template_name='est_app/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property'] = Property.objects.filter(published_date__lte=timezone.now()).order_by('price')[:2]
        return context

    # def get_queryset(self):#show all listings
    #     return Property.objects.filter(published_date__lte=timezone.now())

class AboutView(TemplateView):
    template_name='est_app/about.html'


class PropertyListView(ListView):
    model=Property
    paginate_by = 2

    def get_queryset(self):#show all listings
        return Property.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PropertyDetailView(DetailView,FormMixin):
    model=Property
    form_class=LeadsForm
    # template_name='est_app/property_detail.html'
    redirect_field_name='est_app/property_detail.html'

def propertyDetailView(request,pk):
    # get_object_or_404(Property,pk=pk)
    details={}
    details["property"]=Property.objects.get(pk = pk)
    if request.method =='POST':
        form=LeadsForm(request.POST)
        details["property"]=Property.objects.get(pk = pk)
        
        if form.is_valid():
            lead=form.save(commit=False)
            props=Property.objects.get(pk = pk)
            lead.property=props
            lead.save()

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            emailfrom = form.cleaned_data['email']
            enquiry=form.cleaned_data['message']
            emailto = props.agent.email
            # enquiry=strip_tags(enquiry)

            # enquiry=cleanhtml(enquiry)
            print(enquiry)
            send_mail(
                'New lead from:' +firstname +lastname ,
                f'Message from: {emailfrom} \n \n {enquiry}' ,
                settings.EMAIL_HOST_USER,
                [emailto],
                fail_silently=False,
            )

            # try:
            # except:
            #     pass

            return redirect('property_detail',pk=props.pk)

    elif(request.GET.get('mybtn')):
        form=LeadsForm()
        details["property"]=Property.objects.get(pk = pk)
        details["form"]=form
        return render(request,'est_app/property_detail.html',context=details)

    return render(request,'est_app/property_detail.html',context=details)
 
    

class PropertyCreateView(LoginRequiredMixin, CreateView):
    login_url='/login/'
    form_class= PropertyForm
    redirect_field_name='est_app/property_detail.html'
    model=Property

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    form_class= PropertyForm
    redirect_field_name='est_app/property_detail.html'
    model=Property

class PropertyDeleteView (LoginRequiredMixin, DeleteView):
    model=Property
    success_url=reverse_lazy('property_list')

class PropertyDraftView (LoginRequiredMixin, ListView):
    model=Property
    login_url='/login/'
    # redirect_field_name = 'est_app/ppt_list.html'

    template_name = 'est_app/property_draft_list.html'

    # context_object_name = 'draft_ppt'

    def get_queryset(self):
        return Property.objects.filter(published_date__isnull=True).order_by('created_date')



#main agent views
class AgentListView(ListView):
    model=Agent
    paginate_by = 5

    # def get_queryset(self):#show all listings
    #     return Property.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class AgentDetailView(DetailView):
    model=Agent

class AgentCreateView(LoginRequiredMixin, CreateView):
    login_url='/login/'
    form_class= AgentForm
    redirect_field_name='est_app/agent_list.html'
    model=Agent
    # template_name = 'est_app/agent_form.html'
    # success_url = reverse_lazy('agent_list')



class AgentUpdateView(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    form_class= AgentForm
    redirect_field_name='est_app/agent_detail.html'
    model=Agent

class AgentDeleteView (LoginRequiredMixin, DeleteView):
    model=Agent
    success_url=reverse_lazy('agent_list')

class LeadsListView(ListView):
    model=Leads
    # template_name='est_app/leads_list.html'
    paginate_by = 5



@login_required
def property_publish(request,pk):
    property= get_object_or_404(Property,pk=pk)
    property.publish()
    return redirect('property_detail',pk=pk)

def search_property(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Property.objects.filter(Q(location__contains=query_name)& Q(published_date__lte=timezone.now()))
            if results:
                return render(request, 'est_app/property_search.html', {"results":results})
            elif query_name:
                results = Property.objects.filter(Q(zipcode__exact=query_name) & Q(published_date__lte=timezone.now()))
                if results:
                    return render(request, 'est_app/property_search.html', {"results":results})
                elif query_name:
                    results = Property.objects.filter(Q(rooms__exact=query_name) & Q(published_date__lte=timezone.now()))
                    if results:
                        return render(request, 'est_app/property_search.html', {"results":results})
                    else:
                        return render(request, 'est_app/property_search.html', {"location":query_name})

    
    return render(request, 'est_app/property_search.html', {"location":query_name})

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext



# some unused reference from slack
#  class DetailView(generic.DetailView,FormMixin):
#     model = Album
#     template_name = 'post/detail.html'
#     form_class = SongCreate

#     def get_object(self, *args, **kwargs):
#          pk  =self.kwargs.get('pk')
#          obj = get_object_or_404(Roote, pk=pk)
#          return obj
#     def get_context_data( self, *args, **kwargs ):
#         context =super(DetailView, self).get_context_data(*args, **kwargs)
#         # context['create_form'] = SongCreate()
#         # context['create_url'] = reverse_lazy("post:index")
#         query = self.request.GET.get("q")
#         if query:
#             qs = Album.objects.search(query)
#         return context
#   **def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)