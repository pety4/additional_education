import git
with open("git_url.txt") as source:
    git_url = source.readlines()
result={}
for url in git_url:
    try:
        git.Repo.clone_from(url,f"{url[url.rfind('/')+1]}-https")
    except:
        result[url]='FAIL'
    result[url]='OK'
with open("result.txt") as resultFile:
    for i in result:
        resultFile.write(i)

