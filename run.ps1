docker build -t oreilly-library ./app/.
kubectl apply -f ./kubernetes/mysql/mysql-pv.yaml
kubectl apply -f ./kubernetes/mysql/mysql-deployment.yaml
kubectl apply -f ./kubernetes/deployment.yaml



