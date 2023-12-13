# search an input string in a file and print next 4 lines after the match............

function tbe(){
   merchant="$1"
   if [ "$2" == "" ]; then
       day=$(date +%Y_%m_%d)
   else
       day="$2"
   fi
   app_or_web="$3"
   cd /opt/feed/$merchant/output/promo-analytics/logs
     if [ "$app_or_web" == "app" ]
     then
       log_file=$(ls -ltr *$merchant* | grep brand_promo_app | grep $day | awk '{print $9}')
     else
       log_file=$(ls -ltr *$merchant* | grep brand_promo_$day | grep $day | awk '{print $9}')
     fi
  search_string="$4"

  echo $search_string
  line_number=$(grep -n "$search_string" "$log_file" | cut -d: -f1)

  echo $line_number
    if [ -n "$line_number" ]; then
      # Use awk to print lines starting from the line after the match
        for num in $line_number; do
           awk -v start=$((num + 1)) 'MR >= start && MR <= start + 4  { print $0 "  " }' "$log_file"
        done
    else
        echo "Search string not found in the file."
    fi

}