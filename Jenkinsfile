pipeline {
    agent { docker { image 'frolvlad/alpine-python3' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 bot_main.py'
            }
        }
    }
}