from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Game, Comment
from .forms import GameForm, CommentForm
import random


# Create your views here.

def index(request):
    
    games = Game.objects.order_by('-pk')
    form = GameForm()
    context = {
        'form': form,
        'games' : games,
    }
    return render(request, 'games/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.user = request.user
            game.save()
            return redirect('games:detail', game.pk)
    else:
        form = GameForm()
    context = {
        'form': form,
    }
    return render(request, 'games/create.html', context)



def detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if game.left_number == 0 and game.right_number == 0:
        left = 0
        right = 0
    else:
        left = round(game.left_number / (game.left_number + game.right_number) * 100, 2)

        right = round(game.right_number / (game.left_number + game.right_number) * 100, 2)
    
    comment_form = CommentForm()
    comments = game.comment_set.all()
    context = {
        'game': game,
        'comment_form': comment_form,
        'comments': comments,
        'left' : left,
        'right': right,
    }
    return render(request, 'games/detail.html', context)

@require_POST
def choice(request, pk, pick):

    game = Game.objects.get(pk=pk)
    if pick =='left_side':
        game.left_number += 1
        game.save()
    elif pick == 'right_side':
        game.right_number += 1
        game.save()
    return redirect('games:detail', pk)

@require_POST
def delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.user.is_authenticated:
        if request.user == game.user:
            game.delete()
            return redirect('games:index')
    return redirect('games:detail', game.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.user == game.user:
        if request.method == 'POST':
            form = GameForm(request.POST, instance=game)
            if form.is_valid():
                form.save()
                return redirect('games:detail', game.pk)
        else:
            form = GameForm(instance=game)
    else:
        return redirect('games:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        game = get_object_or_404(Game, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.game = game
            comment.user = request.user
            comment.save()
            return redirect('games:detail', game.pk)
        context = {
            'comment_form': comment_form,
            'game': game,
        }
        return render(request, 'games/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, game_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('games:detail', game_pk)
    # return HttpResponse(status=401)

