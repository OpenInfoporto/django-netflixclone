from __future__ import unicode_literals

from django.db import models

class TVShow(models.Model):

    title = models.CharField('Titolo', max_length=250, null=True)
    story = models.TextField('Trama', null=True)
    cover_image = models.ImageField('Copertina', null=True)

    def __unicode__(self):
        return self.title


class Season(models.Model):

    tvshow = models.ForeignKey(TVShow)
    title = models.CharField('Nome stagione', max_length=250)
    season_number = models.IntegerField('Numero stagione', null=True)

    def __unicode__(self):
        return "%s S. %s" % (self.tvshow, self.season_number)

class Episode(models.Model):

    title = models.CharField('Titolo', max_length=250, null=True)
    story = models.TextField('Trama', null=True)
    episode_number = models.IntegerField('Numero episodio')
    season = models.ForeignKey(Season)
    tvshow = models.ForeignKey(TVShow)

    def __unicode__(self):
        return "%s %sx%s %s" % (self.tvshow, self.season, self.episode_number, self.title)
