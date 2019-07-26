pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                input id: 'Pass arguments', message: 'pass arguments', ok: 'done', parameters: [text(defaultValue: '', description: 'give arguments', name: 'give')]
                sh '''
                sh run.sh $give
                '''
            }
        }
    }
}