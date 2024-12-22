minikube start
minikube image build -t my_jupyter_notebook .
kubectl apply -f configmap.yml
kubectl apply -f pg_secret.yml
kubectl apply -f pg_pvc.yml
kubectl apply -f jupyter_deployment.yml
kubectl apply -f pg_deployment.yml
kubectl apply -f pg_service.yml
kubectl apply -f jupyter_service.yml
kubectl get pods --show-labels
kubectl get services --show-labels
kubectl describe pvc pg_pvc