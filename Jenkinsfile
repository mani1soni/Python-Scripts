pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                sh '''sh run.sh ''' input id: 'Pass arguments', message: 'pass arguments', ok: 'done', parameters: [text(defaultValue: '', description: 'give arguments', name: 'give')]
                
            }
        }
    }
}