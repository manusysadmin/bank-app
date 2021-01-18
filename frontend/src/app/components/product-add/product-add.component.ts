import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.service';

@Component({
  selector: 'app-product-add',
  templateUrl: './product-add.component.html',
  styleUrls: ['./product-add.component.scss']
})
export class ProductAddComponent implements OnInit {

  product = {
    name: '',
    age: '',
    student: false,
    income: ''
  };
  submitted = false;
  public ageBracket = [
    'JUNIOR',
    'ADULT',
    'SENIOR'
  ];
  public incomeBracket = [
    'NO_INCOME',
    'LOW_INCOME',
    'MEDIUM_INCOME',
    'HIGH_INCOME'
  ];
  constructor(private productService: ProductService) { }

  addProduct(): void {
    const data = {
      name: this.product.name,
      age: this.product.age,
      student: this.product.student,
      income: this.product.income
    };

    this.productService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }
  newProduct(): void {
    this.submitted = false;
    this.product = {
      name: '',
      age: '',
      student: false,
      income: ''
    };
  }

  ngOnInit(): void {
  }

}
