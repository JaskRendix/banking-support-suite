import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SupportService } from '../services/support.service';
import { Transaction } from '../models/transaction.model';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent implements OnInit {

  transactions: Transaction[] = [];

  constructor(private supportService: SupportService) {}

  ngOnInit(): void {
    this.supportService.getTransactions().subscribe(data => {
      this.transactions = data;
    });
  }
}
