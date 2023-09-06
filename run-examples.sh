runChainExamples(){
  examples=$(find -s examples/chain_client -type f -mindepth 1 -name '*.py')
  echo "Running all chain examples..."
  for example in $examples
  do
    echo "$example"
  	python $example
    echo "============================================================="
  done
}

runExchangeExamples(){
  dirs=$(find -s examples/exchange_client -type d -mindepth 1)
  for dir in $dirs
  do
    examples=$(find -s $dir -type f -name '*.py')
    echo "Running $dir examples..."
    for example in $examples
    do
        echo $example
        # auto kill after 5s to exit streaming examples
        (sleep 5 && pkill -f $example) &
        python $example
        echo "============================================================="
    done
  done
}

export PYTHONPATH=$PYTHONPATH:$(pwd)

TYPE=$1
case $TYPE in
  "chain")
    runChainExamples
    ;;

  "exchange")
    runExchangeExamples
    ;;

  *)
    echo "Missing required argument, must be \"chain\" or \"exchange\""
    ;;
esac
