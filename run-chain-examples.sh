for i in {1..17}
do
  echo "running example ${i}"
	python examples/chain_client_examples/${i}_*
  echo "============================================================="
done
