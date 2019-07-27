
pipeline{
    agent any
    stages{
        stage("test"){
            steps{
                script{
                    def output=input message: 'give arguments', ok: 'done', parameters: [string(defaultValue: '', description: '', name: 'SOMETHING', trim: false)]
                }
                
                sh "echo ${output}"
                
            }
        }
    }
}