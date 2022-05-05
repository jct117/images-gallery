import React from "react";
import { Button } from "react-bootstrap";

const Welcome = () => (
  <div class="bg-light p-5 rounded-lg m-3">
    <h1 class="display-4">Images Gallery!</h1>
    <p class="lead">
      This is a simple application that retrieves photos using Unsplash api.
      Enter any serach term in the input field.
    </p>
    <hr class="my-4" />

    <Button variant="primary" href="https://unsplash.com" target="_blank">
      Learn More Shit
    </Button>
  </div>
);

export default Welcome;
