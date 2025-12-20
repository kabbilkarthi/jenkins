pipeline {
    agent { label 'controller' }

    stages {
        stage('Run script') {
            steps {
                sh '''
                    echo "Running on: $(hostname -f)"
                    uname -a

                    # Your Linux scripting here
                    df -h
                    free -m
                '''
            }
        }
    }
}
