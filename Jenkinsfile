pipeline{
    agent any
    stages{
        stage("test"){
            OUTPUT = input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]
            steps{
                sh '''
                sh run.sh $OUTPUT
                '''
            }
        }
    }
}