pipeline {
  agent any
  stages {
    stage ('Branch update') {
      when { not { branch 'master' } }
      steps {
        withCredentials([usernamePassword(credentialsId: 'github', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh "git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/ivanmtoroc/superdrogas.git"
          sh 'git config --add remote.origin.fetch +refs/heads/master:refs/remotes/origin/master'
          sh 'git fetch --no-tags'
          sh "git checkout origin/${env.BRANCH_NAME}"
          sh 'git pull'
        }
      }
    }
    stage ('Run tests') {
      when { not { branch 'master' } }
      steps {
        sh 'dropdb --if-exist test_superdrogas'
        sh 'virtualenv env -p python3'
        sh '. env/bin/activate'
        sh 'pip3 install -r requirements.txt'
        sh 'python3 manage.py makemigrations'
        sh 'python3 manage.py migrate'
        sh 'python3 manage.py test'
        sh '''
        if [ "$?" = "0" ]; then
            printf "Test: Success.\n"
        else
            printf "Test: Failed.\n"
            exit 1
        fi
        '''
      }
    }
    stage ('Continuous integration') {
      when { not { branch 'master' } }
      steps {
        withCredentials([usernamePassword(credentialsId: 'github', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh "git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/ivanmtoroc/superdrogas.git"
          sh 'git config --add remote.origin.fetch +refs/heads/master:refs/remotes/origin/master'
          sh 'git fetch --no-tags'
          sh 'git checkout origin/master'
          sh "git merge origin/${env.BRANCH_NAME}"
          sh 'git push origin HEAD:master'
        }
      }
    }
  }
}