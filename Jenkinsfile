pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                sh '''sh run.sh''' 
                input id: 'Pass arguments', message: 'pass arguments', ok: 'done', parameters: [string(defaultValue: 'string', description: 'string', name: 'string', trim: false)]
            }
        }
    }
}