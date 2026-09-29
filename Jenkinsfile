pipeline {
    agent any

    // Check GitHub every 2 minutes; build automatically when a new commit appears
    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the same repo/branch configured in the job ("Pipeline script from SCM")
                checkout scm
                sh 'git log -1 --oneline'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest -v'
            }
        }
    }

    post {
        success { echo 'Pipeline finished: SUCCESS' }
        failure { echo 'Pipeline finished: FAILURE' }
    }
}
