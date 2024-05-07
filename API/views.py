from django.shortcuts import render
import csv
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

updated_data = []

# Create your views here.

def homepage(request):
    return render(request, 'api/WebPage.html')

def patient(request):
    import requests
    from fhir.resources import construct_fhir_element, patient

    # URL del server FHIR
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "Patient"

    # Effettua la richiesta GET per ottenere le risorse Patient
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                patients = []
                for patient_data in data['entry']:
                    patients.append(patient_data.get('resource'))

                if patients:
                    for patient_data in patients:
                        try:
                            patientX = patient.Patient.parse_obj(patient_data)
                            if ((patientX.name[0].given[0] != None) or (patientX.name[0].given[0] != '') or (patientX.name[0].family != None) or (patientX.name[0].family != '')):
                                updated_data.append(patientX)

                        except Exception as e:
                            continue
                else:
                    print("Nessun paziente trovato.")
            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)
    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/WebPage.html', {'updated_data': updated_data})

def careplan1(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["455","CR Cervello","455","CR Inguine"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "455":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record1.html', context)

def careplan2(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["509","RX MAMMOGRAFIA BILATERALE","509","CR Anca sinistra"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "509":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record2.html', context)

def careplan3(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1119","CR Cervello"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1119":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record3.html', context)

def careplan4(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1302","CR Busto"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1302":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record4.html', context)

def careplan5(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1503","CR Cervello"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1503":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record5.html', context)

def careplan6(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1505","CR Anca"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1505":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record6.html', context)

def careplan7(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1554","CR body"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1554":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)
        
        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record7.html', context)

def careplan8(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1555","CR Rotula sinistra"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1555":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record8.html', context)

def careplan9(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1110","CR Prostata"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1110":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record9.html', context)

def careplan10(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1612","CR body"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1612":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record10.html', context)

def careplan11(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1653","CR Occhio"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1653":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)

        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record11.html', context)

def careplan12(request):
    import requests
    from fhir.resources import careplan

    # URL del server FHIR di test
    base_url = "http://hapi.fhir.org/baseR5"
    resource_type = "CarePlan"

    subject_references = ["455", "509", "1119","1302", "1503", "1505","1554", "1555", "1110","1612", "1653", "1756"]
    images = ["1756","CR Cervello"]
    num_subject_references = len(subject_references)

    # Effettua la richiesta GET per ottenere le risorse CarePlan
    url = f"{base_url}/{resource_type}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'entry' in data:
                care_plans = []
                for care_plan_data in data['entry']:
                    care_plans.append(care_plan_data.get('resource'))

                updated_data2 = []
                if care_plans:
                    subject_reference_index = 0

                    for care_plan_data in care_plans:
                        try:
                            if 'subject' in care_plan_data:
                                care_plan_obj = careplan.CarePlan.parse_obj(care_plan_data)
                                care_plan_obj.subject.reference = subject_references[subject_reference_index]
                                subject_reference_index = (subject_reference_index + 1) % num_subject_references
                                if care_plan_obj.subject.reference == "1756":
                                    updated_data2.append(care_plan_obj)
                                              
                        except Exception as e:
                            print("Errore durante l'analisi del CarePlan:", e)
                            continue

                else:
                    print("Nessun CarePlan trovato.")

            else:
                print("Nessuna risorsa 'entry' trovata nella risposta.")
        except Exception as e:
            print("Errore durante l'analisi della risposta JSON:", e)
            print("Risposta JSON:", response.text)
        
        context = {
            'updated_data2': updated_data2,
            'images': images,
        }

    else:
        print(f"Errore: {response.status_code}")

    return render(request,'api/Record12.html', context)

@csrf_exempt
def esporta_csv(request):

    if request.method == 'POST':
        data1 = request.POST.get('data')
        data1 = json.loads(data1)

        with open('datiPaziente.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            for riga in data1:
                writer.writerow(riga)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Metodo non consentito'}, status=405)

@csrf_exempt
def esporta_csv2(request2):

    if request2.method == 'POST':
        data2 = request2.POST.get('data')
        data2 = json.loads(data2)

        with open('datiCarePlan.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            for riga in data2:
                writer.writerow(riga)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Metodo non consentito'}, status=405)

@csrf_exempt
def esporta_csv3(request3):

    if request3.method == 'POST':
        data3 = request3.POST.get('data')
        data3 = json.loads(data3)

        with open('datiStudi.csv', mode='a', newline='') as file:
            writer = csv.writer(file)

            for riga in data3:
                writer.writerow(riga)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Metodo non consentito'}, status=405)


