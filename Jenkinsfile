pipeline{
    agent any
   environment {
        //once you sign up for Docker hub, use that user_id here
        registry = "yasantha1995/networkautomation"
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'Docke_Cred'
        dockerImage = ''
    }
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
                sh "docker build -t yasantha1995/networkautomation  /var/lib/jenkins/workspace/netDevOps/EtherchannelConfig/"
            }
        }
        stage('Upload Image') {
            steps{
                echo "Image is pushing...."
                sh "docker login -u yasantha1995 -p Yasa@1995"
                sh "docker push yasantha1995/networkautomation"
                echo "Image pushed."
      }
    }
        stage('Docker prune'){
            steps{
                sh "docker system prune -f"
            }
        }
    }
    
}