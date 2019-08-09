def browser = 'unknown'
pipeline{
    agent any
    stages{
        stage("test"){
            environment {
                MY_ENV = 'hi' 
            }
            steps{
                
                    sh '''
                    sh run.sh 
                    '''
                script{
                    browser = sh(returnStdout: true, script: 'echo Chrome')
                }
                
            }
        }
        stage("test2"){
            environment {
                MY_ENV = 'hello'
            }
            steps{
                sh '''
                sh run.sh
                '''
            }
        }
    }
}