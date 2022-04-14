from django.shortcuts import render, redirect
from .models import Vote, Comment
from .forms import VoteForm, CommentForm
from django import forms
from django.views.decorators.http import require_http_methods, require_safe, require_POST
import random

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    rand_vote = Vote.objects.get(pk=random.choice(Vote.objects.values_list('pk'))[0])

    context = {
        'votes':votes,
        'rand_vote':rand_vote,
    }

    return render(request, 'votes/index.html', context)


def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    else:
        form = VoteForm()

    context = {
        'form':form
    }

    return render(request, 'votes/create.html', context)


def detail(request, pk):
    options =  [(Vote.objects.filter(pk=pk).values_list('choice_one')[0][0],Vote.objects.filter(pk=pk).values_list('choice_one')[0][0]),
         (Vote.objects.filter(pk=pk).values_list('choice_two')[0][0], Vote.objects.filter(pk=pk).values_list('choice_two')[0][0])]

    vote = Vote.objects.get(pk=pk)
    form = CommentForm()
    form.fields['choice'].widget.choices = options
    comments = vote.comment_set.all()
        

    context = {
        'vote':vote,
        'form':form,
        'comments':comments,
    }

    return render(request, 'votes/detail.html', context)


def detail_result(request, pk):
    vote = Vote.objects.get(pk=pk)
    if request.POST:
        if request.POST['choice'] == vote.choice_one:
            vote.vote_one += 1

        elif request.POST['choice'] == vote.choice_two:
            vote.vote_two += 1

        vote.save()

    options =  [(Vote.objects.filter(pk=pk).values_list('choice_one')[0][0],Vote.objects.filter(pk=pk).values_list('choice_one')[0][0]),
         (Vote.objects.filter(pk=pk).values_list('choice_two')[0][0], Vote.objects.filter(pk=pk).values_list('choice_two')[0][0])]

    form = CommentForm()
    form.fields['choice'].widget.choices = options
    comments = vote.comment_set.all()
    tot = vote.vote_one + vote.vote_two
    one_per = 0
    two_per = 0
    if tot:
        one_per = round(vote.vote_one/tot * 100,2)
        two_per = round(100 - one_per,2)

    context = {
        'vote':vote,
        'form':form,
        'comments':comments,
        'one_per':one_per,
        'two_per':two_per,
    }

    return render(request, 'votes/detail_result.html', context)


@require_POST
def create_comment(request, pk):
    vote = Vote.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.vote = vote
        comment.save()

    return redirect('votes:detail', pk)


@require_POST
def delete(request, pk):
    vote = Vote.objects.get(pk=pk)
    vote.delete()

    return redirect('votes:index')