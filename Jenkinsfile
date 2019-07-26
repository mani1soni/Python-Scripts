pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                input id: 'Pass arguments', message: 'pass arguments', ok: 'done', parameters: [choice(choices: ['$1', '$2'], description: '', name: 'agruments')]
                sh '''sh run.sh '''
            }
        }
    }
}