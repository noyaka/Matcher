from django.shortcuts import render
from .models import Candidate, Skill, Job

def skill(request):
    data = Skill.objects.all()
    return render(request, "skill.html", {"skills":data})

def job(request):
    data = Job.objects.all()
    return render(request, "job.html", {"jobs": data})

def candidate(request, pk):
    # get the specific job
    job_obj = Job.objects.get(pk=pk)
    job_skills = job_obj.skill.all()
    len_job_skills = len(job_skills)

    # dict that contains candidates and score for each candidate
    can_dict = {}
    # get the candidates with the same title as the job's title
    data = Candidate.objects.filter(slug=job_obj.slug)

    if len_job_skills == 0:
        best_candidate = list(data)
    else:
        for candidate in data:
            counter = 0
            can_skills = candidate.skill.all()
            if len(can_skills) == 0:
                continue
            for skill in list(can_skills):
                if skill in job_skills:
                    counter += 1
            if (counter/len_job_skills) >= 0.5:
                can_dict[candidate] = counter/len_job_skills
        can_dict = dict(sorted(can_dict.items(), key=lambda item: item[1], reverse=True))

        best_candidate = can_dict.keys()

    return render(request, "candidate.html", {"candidates": best_candidate})