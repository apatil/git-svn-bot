import feedparser
import time
import os

__all__ = ['sync']

def svn2git():
    print 'Svn repo updated, pushing to git'
    
    print 'Fetching'
    os.system('git svn fetch')

    print 'Rebasing'
    os.system('git svn rebase')
    
    print 'Pulling just to be safe'
    os.system('git pull origin master')
    
    print 'Pushing'
    os.system('git push origin master')
    
    print 'Done'

def up(url):
    return feedparser.parse(url).feed.updated_parsed
    
def git2svn():
    print 'Git repo updated, pushing to svn'
    print 'Pulling'
    os.system('git pull origin master')
    
    print 'Committing'
    os.system('git svn dcommit')
    

def sync(svn_url, git_url, interval=60):
    
    svn_last_update = up(svn_url)
    git_last_update = up(git_url)
    
    while True:
        time.sleep(interval)
        
        svn_cur_update = up(svn_url)
        git_cur_update = up(git_url)
        
        if svn_cur_update != svn_last_update:
            svn2git()
            svn_last_update = svn_cur_update
            
        if git_cur_update != git_last_update:
            git2svn()
            git_last_update = git_cur_update