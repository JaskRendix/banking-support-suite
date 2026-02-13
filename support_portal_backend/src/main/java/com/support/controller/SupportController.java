package com.support.controller;

import com.support.model.Transaction;
import com.support.repository.TransactionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/support")
public class SupportController {

    @Autowired
    private TransactionRepository repository;

    @GetMapping("/health")
    public String getSystemStatus() {
        return "Support API is UP and connected to Risk Engine";
    }

    @GetMapping("/transactions/failed")
    public List<Transaction> getFailedTransactions() {
        // As a Support Tech, you want to see what broke first!
        return repository.findByStatus("FAILED");
    }
}
