node {
    agent any
    environment {
        registry = "https://279773871986.dkr.ecr.us-east-2.amazonaws.com/oasisbot"
        registryCredential = 'ecr:us-east-2:ecr'
        dockerImage = ""
    }
    stages {
        stage('Pull from Repo') {
            steps {
                checkout scm
            }
        }
        stage('Build Container') {
            steps {
                script {
                    dockerImage = docker.build('279773871986.dkr.ecr.us-east-2.amazonaws.com/oasisbot:latest')
                }
            }
        }
        stage('Stage Container Image') {
            
                docker.withRegistry(registry,registryCredential) {
                    dockerImage.push()
                
            }
        }
    }
}