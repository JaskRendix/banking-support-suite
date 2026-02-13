package com.support.controller;

import com.support.model.Transaction;
import com.support.repository.TransactionRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/support")
@CrossOrigin(origins = "*")
public class TransactionController {

    private final TransactionRepository repository;

    public TransactionController(TransactionRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/transactions")
    public List<Transaction> getAllTransactions() {
        return repository.findAll();
    }

    @GetMapping("/transactions/status/{status}")
    public List<Transaction> getTransactionsByStatus(@PathVariable String status) {
        return repository.findByStatus(status);
    }
}
