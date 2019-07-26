pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                input message: 'Write some thing', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]                
                sh '''
                sh run.sh $SOMETHING
                '''
            }
        }
    }
}