package com.support.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.support.model.Transaction;
import java.util.List;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {
    List<Transaction> findByStatus(String status);
}
