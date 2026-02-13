package com.support.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "transactions")
@Data // Generates getters/setters via Lombok
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    private String transactionRef;
    private String status; // e.g., "PROCESSED", "FAILED", "PENDING"
    private Double exposureAmount;
    private String errorCode; // Crucial for Support technicians
}