import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  // A number specifying the number of VUs to run concurrently.
  vus: 10,
  // A string specifying the total duration of the test run.
  duration: '30s',
}

  export default function() {
  http.get('https://www.jumia.com.ng/mlp-holiday-feasting/');
  sleep(1);
}
