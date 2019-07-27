pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                OUTPUT=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]
                sh '''
                sh run.sh $OUTPUT
                '''
            }
        }
    }
}