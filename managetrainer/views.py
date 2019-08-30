from django.http import HttpResponse
from . models import Trainer
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from . forms import UserForm


def home(request):
    return HttpResponse("<h1> Welcome to Home Page </h1>")


class TrainerDetails(generic.ListView):
    template_name = 'trainerhome.html'
    context_object_name = 'trainers_data'

    def get_queryset(self):
        return Trainer.objects.all()


class TrainerInfo(generic.DetailView):
    model = Trainer
    template_name = 'trainerinfo.html'

# def trainer_home(request):
#
#     ''' all_trainers = Trainer.objects.all()
#     html = ''
#
#     for trainer in all_trainers:
#         url = '<a href = '+str(trainer.emp_id)+'>'+str(trainer.emp_name)+'</a> <br>'
#         html = html + url
#
#     print(html)
#     return HttpResponse(html)
#     '''
#     all_trainers = Trainer.objects.all()
#     return render(request, 'trainerhome.html', {'trainers_data': all_trainers})
#
#
# def trainer_details(request, emp_id):
#
#     '''
#
#     try:
#         trainer = Trainer.objects.get(emp_id=emp_id)
#     except Trainer.DoesNotExist:
#         raise Http404("Trainer Does Not Exist")
#
#     '''
#
#     trainer = get_object_or_404(Trainer, emp_id=emp_id)
#
#     return render(request, 'trainerinfo.html', {'trainer': trainer})
#
#
# def trainer_change(request, emp_id):
#
#     trainer = get_object_or_404(Trainer, emp_id=emp_id)
#     batch_code = request.POST.get('change_status')
#     try:
#         batch = trainer.batches_set.get(batch_code=batch_code)
#     except Batches.DoesNotExist:
#         return render(request, 'trainerinfo.html', {'trainer': trainer, 'msg': "Batch Does Not exist"})
#     else:
#         if batch.status:
#             return render(request, 'trainerinfo.html',
#                           {'trainer': trainer, 'msg': "Updation Not Required"})
#         batch.status = True
#         batch.save()
#         return render(request, 'trainerinfo.html', {'trainer': trainer, 'msg': 'Batch Updation Successful'})
#
#
# def register_page(request):
#      return render(request, 'register.html')
#
#
# def add_trainer(request):
#
#      emp_id = request.POST['emp_id']
#      emp_name = request.POST['emp_name']
#      gender = request.POST['gender']
#      salary = float(request.POST['salary'])
#      var = str(request.POST['doj']).split('-')
#
#      year = int(var[0])
#      month = int(var[1])
#      day = int(var[2])
#
#      trainer_obj = Trainer(emp_id=emp_id, emp_name=emp_name, gender=gender, salary=salary, doj=date(year, month, day))
#
#      trainer_obj.save()
#
#      return render(request, 'trainerhome.html')


class CreateForm(CreateView):
    model = Trainer
    fields = ['emp_id', 'emp_name', 'gender', 'salary', 'doj', 'profile_pic']
    template_name = 'register.html'
    #context_object_name = 'trainer_fields' // default context name is form


class UpdateForm(UpdateView):
    model = Trainer
    fields = ['emp_id', 'emp_name', 'gender', 'salary', 'doj']
    template_name = 'update.html'


class DeleteForm(DeleteView):
    model = Trainer
    success_url = reverse_lazy('managetrainer:home')


class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('managetrainer:home')

        return render(request, self.template_name, {'form': form})
