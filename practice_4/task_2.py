import git
with open("git_url.txt") as source:
    git_url = source.readlines()
result={}
for url in git_url:
    url.rstrip()
    try:
        git.Repo.clone_from(url,f"{url[url.rfind('/')+1]}-https")
        result[url] = 'OK'
    except:
        result[url]='FAIL'
with open("result.txt", "w") as resultFile:
    for i in git_url:
        resultFile.write(f"{i}\t")
        resultFile.write(f"{result[i]}\n")

