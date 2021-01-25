import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-product-add',
  templateUrl: './product-add.component.html',
  styleUrls: ['./product-add.component.scss']
})
export class ProductAddComponent implements OnInit {

  productForm: FormGroup;

  product = {
    name: '',
    age: '',
    student: false,
    income: ''
  };

  submitted = false;

  public ageBrackets = {
    '0-17': 'JUNIOR',
    '18-64': 'ADULT',
    '65+': 'SENIOR'
  };

  public incomeBrackets = {
    '0': 'NO_INCOME',
    '1-12000': 'LOW_INCOME',
    '12001-40000': 'MEDIUM_INCOME',
    '40000+': 'HIGH_INCOME'
  };

  constructor(private productService: ProductService,
              private fb: FormBuilder) {
    this.productForm = this.fb.group({
      name: ['', Validators.required],
      ageBracket: ['', Validators.required],
      incomeBracket: ['', Validators.required],
      student: ['', Validators.required]
    });
  }

  get name(): any {
    return this.productForm.get('name');
  }

  get ageBracket(): any {
    return this.productForm.get('ageBracket');
  }
  get incomeBracket(): any {
    return this.productForm.get('incomeBracket');
  }
  get student(): any {
    return this.productForm.get('student');
  }

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

  ngOnInit(): void {
  }

}
