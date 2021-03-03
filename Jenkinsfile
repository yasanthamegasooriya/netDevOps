pipeline{
    agent any
    stages{
        stage('clear workspcace'){
            steps{
                deleteDir()
                sh 'ls -lah'
                
            }
            
        }
        stage('Git pulling'){
            steps{
                echo "git pulling.."
                git branch: 'main', credentialsId: 'gitCred', url: 'https://github.com/yasa1995/netDevOps.git'
                
            }
        }
        stage('Docker image build'){
            steps{
                echo "Images is building ..."
                sh "docker build -t networkautomation/etherchannel  /var/lib/jenkins/workspace/netDevOps/EtherchannelConfig/"
            }
        }
        stage('Third'){
            steps{
                echo "hi Third stage"
            }
        }
        stage('Forth'){
            steps{
                echo "hi Forth stage"
            }
        }
    }
    
}