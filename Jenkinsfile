pipeline {
  agent {
    node {
      label "docker-agent-python-node"
    }
  }
  triggers {
    pollSCM "*/5 * * * *"
  }
  stages {
    stage("Build Python") {
      steps {
        sh "pip3 install --ignore-installed -r requirements.txt"
      }
    }
    stage("Test Python") {
      steps {
        sh "pytest tests/"
      }
    }
  }
}