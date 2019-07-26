pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)], submitterParameter: 'SOMETHING'
                sh '''
                sh run.sh $SOMETHING
                '''
            }
        }
    }
}