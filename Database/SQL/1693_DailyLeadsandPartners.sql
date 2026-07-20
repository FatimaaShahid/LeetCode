SELECT date_id, make_name, COUNT(DISTINCT(Lead_id)) AS unique_leads,COUNT(DISTINCT(partner_id)) AS unique_partners
FROM DailySales
Group By date_id,make_name;
