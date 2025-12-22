pipeline {
    agent { label 'controller' }

    stages {
        stage('Confirm run') {
            steps {
                script {
                    input message: 'Continue to next stage?'
                }
            }
        }

        stage('Run script') {
            steps {
                sh '''
                    echo "Running on: $(hostname -f)"
                    uname -a

                    df -h
                    free -m
                    du -ahd1 /tmp
                '''
            }
        }
    }
}
