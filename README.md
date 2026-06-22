Alembic for make migrations:
    alembic init -t async migrations  
    alembic stamp head
    alembic revision --autogenerate -m "init"
    alembic upgrade head



Create new branch:
    git switch -c folder/branch-name

For chechking out: 
    git checkout feature/UserAuth    

git add .
git commit -m "msg"
git push