pipeline {
  environment {
    registry = "registry.hub.docker.com"
    registryCredential = 'dockerhub2'
    imgName = 'robmaynardjr/oasisbot:latest'
    gitRepo = "https://github.com/robmaynardjr/OasisBot.git"
    smartCheckHost = "10.0.10.100"
  }
  
    agent { label 'jenkins-jenkins-slave ' }

    stages {
        stage("Building image") {
            steps{
                container('jnlp') {
                    script {
                        sh "curl -O https://s3.us-east-2.amazonaws.com/artifacts.trend-demolab.com/configs/config.cfg"
                        dockerImage = docker.build(imgName)
                    }
                }
            }
        }

        stage("Stage Image") {
            steps{
                container('jnlp') {
                    script {
                        withCredentials([
                            usernamePassword([
                                credentialsId: 'dockerhub2', 
                                passwordVariable: 'PASS', 
                                usernameVariable: 'USER',
                                ])
                            ]) {

                            // docker.withRegistry('', registryCredential ) {
                            //     dockerImage.push()
                            echo "Logging into Dockerhub..."
                            sh "docker login -u '${USER}' -p '${PASS}'"
                            echo "Pushing Image..."
                            sh "docker push ${imgName}"                       
                            }
                        }   
                    }
                }
            }
        stage("Security Check") {
            steps {
                container('jnlp') {
                    script {
                        withCredentials([
                            usernamePassword([
                                credentialsId: "dockerhub2",
                                usernameVariable: "USER",
                                passwordVariable: "PASSWORD",
                            ]),
                            usernamePassword([
                                credentialsId: "smart-check-jenkins-user",
                                usernameVariable: "SCUSER",
                                passwordVariable: "SCPASSWORD",
                            ])   
                        ]){
                            sh "docker login -u '${USER}' -p '${PASSWORD}'"
                            def imgPAuth = " {\"username\":\"${USER}\",\"password\":\"${PASSWORD}\"} "
                            def findings =  " {\"malware\":0,\"vulnerabilities\":{\"defcon1\":0,\"critical\":20,\"high\":200},\"contents\":{\"defcon1\":0,\"critical\":0,\"high\":5},\"checklists\":{\"defcon1\":0,\"critical\":0,\"high\":0} } "
                            sh "docker run deepsecurity/smartcheck-scan-action --image-name registry.hub.docker.com/robmaynardjr/oasisbot:latest --smartcheck-host=10.0.10.100 --smartcheck-user='$SCUSER' --smartcheck-password='${SCPASSWORD}' --insecure-skip-tls-verify --findings-threshold='${findings}' --image-pull-auth='${imgPAuth}'"
                        }
                    }
                }
            }
        }

        stage ("Deploy to Cluster") {
            steps{
                container('jnlp') {
                    script {
                        sh "kubectl delete deployment oasisbot"
                        sh "sleep 10"
                        sh "kubectl apply -f oasisbot.yaml"
                    }
                }
            }
        }   
    }
}