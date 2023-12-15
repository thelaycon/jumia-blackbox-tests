# Jumia Holiday Sales Testing

This Github project is a blackbox test of the Jumia e-commerce website and a load testing analysis for the December festive period. The blackbox testing is a prototype of how to identify any potential issues in the functionality of the Jumia e-commerce website, ensuring a smooth user experience for customers. 

Additionally, the load testing analysis will help determine if the website can handle increased traffic during the busy December festive period, ensuring it remains responsive and accessible to all users. 


![Jumia](https://logos-world.net/wp-content/uploads/2022/12/Jumia-Logo.png) ![Playwright](https://miro.medium.com/v2/resize:fit:953/0*w_ivMwMdr2YvH8bB.png) ![k6](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_9fcecb565c7303e367747d46e315effe/k6.png)

## Running Tests

To run tests, run the following command

```bash
  pip install -r requiremennts
  python -m pytest --html=report.html
```

To run the load tests, you must have xk6 (k6 modified) installed. Then:

```bash
    k6 run --out dashboard=export=test-report.html script.js
```


## Summary of Load Testing
![k6](performance-report.png)
